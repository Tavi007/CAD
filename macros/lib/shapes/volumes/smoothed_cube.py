class RoundedBox:
    """
    A box defined by length (X), width (Y), and height (Z).

    The edge radii describe:
        top_radius    - edges at the top Z plane
        side_radius   - edges along the sides / intermediate edges
        bottom_radius - edges at the bottom Z plane

    The class can create a raw box or a rounded box.
    """

    def __init__(
        self,
        length,
        width,
        height,
        top_radius=0.0,
        side_radius=0.0,
        bottom_radius=0.0,
        origin=None,
        name="RoundedBox",
    ):
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)

        self.top_radius = float(top_radius)
        self.side_radius = float(side_radius)
        self.bottom_radius = float(bottom_radius)

        self.origin = origin or App.Vector(0, 0, 0)
        self.name = name

        self._validate()

    def _validate(self):
        for key in ("length", "width", "height"):
            value = getattr(self, key)
            if not math.isfinite(value) or value <= 0:
                raise ValueError(key + " must be positive and finite.")

        for key in ("top_radius", "side_radius", "bottom_radius"):
            value = getattr(self, key)
            if not math.isfinite(value) or value < 0:
                raise ValueError(key + " must be non-negative and finite.")

    def create_raw(self):
        """Create the unrounded Part box."""
        return Part.makeBox(
            self.length,
            self.width,
            self.height,
            self.origin,
        )

    def radius_for_edge(self, edge, top_z=None, bottom_z=None):
        """
        Determine the radius for an original, unfilleted edge.

        This is a geometric classification, not a semantic edge
        label. Edges lying in the top or bottom planes receive
        those radii; all others receive the side radius.
        """
        scale = max(
            1.0, self.length, self.width, self.height
        )
        tol = scale * 1e-7

        if top_z is None:
            top_z = self.origin.z + self.height
        if bottom_z is None:
            bottom_z = self.origin.z

        bb = edge.BoundBox

        if (
            abs(bb.ZMin - top_z) < tol
            and abs(bb.ZMax - top_z) < tol
        ):
            return self.top_radius

        if (
            abs(bb.ZMin - bottom_z) < tol
            and abs(bb.ZMax - bottom_z) < tol
        ):
            return self.bottom_radius

        return self.side_radius

    def create_rounded(self):
        """
        Create a rounded standalone box.

        For mixed radii, the edges are processed in descending
        radius order. Failed fillets are reported.
        """
        shape = self.create_raw()
        top_z = self.origin.z + self.height
        bottom_z = self.origin.z

        # Capture original edge bounding boxes and their radii.
        edge_specs = []
        for edge in shape.Edges:
            edge_specs.append((
                edge.BoundBox,
                self.radius_for_edge(edge, top_z, bottom_z),
            ))

        edge_specs.sort(key=lambda item: item[1], reverse=True)

        for bb0, radius in edge_specs:
            if radius <= 0:
                continue

            # Find a current edge matching the original bounds.
            target = None
            for edge in shape.Edges:
                bb = edge.BoundBox
                if (
                    abs(bb.XMin - bb0.XMin) < 1e-7
                    and abs(bb.XMax - bb0.XMax) < 1e-7
                    and abs(bb.YMin - bb0.YMin) < 1e-7
                    and abs(bb.YMax - bb0.YMax) < 1e-7
                    and abs(bb.ZMin - bb0.ZMin) < 1e-7
                    and abs(bb.ZMax - bb0.ZMax) < 1e-7
                ):
                    target = edge
                    break

            if target is None:
                continue

            try:
                result = shape.makeFillet(radius, [target])
                if result.isValid() and not result.isNull():
                    shape = result
            except Exception as exc:
                App.Console.PrintWarning(
                    self.name + ": fillet failed (radius "
                    + str(radius) + "): " + str(exc) + "\n"
                )

        return shape
