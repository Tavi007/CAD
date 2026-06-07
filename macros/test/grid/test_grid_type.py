import numpy as np
from math import cos, sin

from lib.grid.grid_type import GridType, GRID_TYPES, PI3


class TestGetUnitVector:
    def test_orthogonal_unit_vector(self):
        result = GridType.ORTHOGONAL.get_unit_vector()
        expected = np.array([
            [1.0, 0.0],
            [0.0, 1.0],
        ])
        np.testing.assert_allclose(result, expected)

    def test_packed_unit_vector(self):
        result = GridType.PACKED.get_unit_vector()
        expected = np.array([
            [1.0, cos(PI3)],
            [0.0, sin(PI3)],
        ])
        np.testing.assert_allclose(result, expected)


class TestGetSymmetries:
    def test_orthogonal_returns_empty_list(self):
        indices = [(1, 2), (3, 4)]
        result = GridType.ORTHOGONAL.get_symmetries(indices)
        assert result == []

    def test_packed_returns_12_symmetries(self):
        indices = [(1, 2)]
        result = GridType.PACKED.get_symmetries(indices)
        assert len(result) == 12

    def test_packed_identity_symmetry(self):
        indices = [(1, 2), (3, 4)]
        result = GridType.PACKED.get_symmetries(indices)
        assert result[0] == [(1, 2), (3, 4)]

    def test_packed_middle(self):
        indices = [(0, 0)]
        result = GridType.PACKED.get_symmetries(indices)
        expected = set([frozenset([(0, 0)])])
        assert result == expected

    def test_packed_one_off(self):
        indices = [(1, 0)]
        result = GridType.PACKED.get_symmetries(indices)
        expected = set([
            frozenset([(1, 0)]),
            frozenset([(1, -1)]),
            frozenset([(0, -1)]),
            frozenset([(-1, 0)]),
            frozenset([(-1, -1)]),
            frozenset([(0, 1)])
        ])
        assert result == expected

    def test_packed_second_symmetry(self):
        indices = [(1, 2)]
        result = GridType.PACKED.get_symmetries(indices)
        assert result[1] == [(1, -3)]  # (x, -x-y)

    def test_packed_third_symmetry(self):
        indices = [(1, 2)]
        result = GridType.PACKED.get_symmetries(indices)
        assert result[2] == [(-1, -2)]  # (-x, -y)

    def test_packed_all_symmetries_are_unique_for_general_point(self):
        indices = [(2, 3)]
        result = GridType.PACKED.get_symmetries(indices)
        unique = {tuple(sym[0]) for sym in result}
        assert len(unique) == 12

    def test_packed_applies_transform_to_all_points(self):
        indices = [(1, 2), (3, 4)]
        result = GridType.PACKED.get_symmetries(indices)
        # symmetry #2: (-x, -y)
        expected = [
            (-1, -2),
            (-3, -4),
        ]
        assert result[2] == expected


class TestGridTypes:
    def test_grid_types_contains_all_types(self):
        assert GRID_TYPES == [
            GridType.ORTHOGONAL,
            GridType.PACKED,
        ]
