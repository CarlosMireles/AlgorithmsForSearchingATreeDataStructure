import unittest
import search


class MyTestCaseForMtoF(unittest.TestCase):

    def setUp(self):
        starting_city = 'M'
        goal_city = 'F'
        self.problem_to_resolve = search.GPSProblem(starting_city, goal_city, search.romania)

    def test_going_from_M_to_F_breath_first(self):
        broad = search.breadth_first_graph_search(self.problem_to_resolve)

        self.assertEqual(broad[1], 31, "It should have generated 31 nodes")
        self.assertEqual(broad[2], 23, "It should have visited 23 nodes")
        self.assertEqual(broad[3], 520, "The total cost is 520")

        route = ["<Node F>", "<Node S>", "<Node R>", "<Node C>", "<Node D>", "<Node M>"]
        nodes_str = [str(node) for node in broad[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_M_to_F_deep_first(self):
        deep = search.depth_first_graph_search(self.problem_to_resolve)
        self.assertEqual(deep[1], 29, "It should have generated 29 nodes")
        self.assertEqual(deep[2], 18, "It should have visited 18 nodes")
        self.assertEqual(deep[3], 928, "The total cost is 928")

        route = ["<Node F>", "<Node B>", "<Node P>", "<Node R>", "<Node S>", "<Node A>", "<Node T>", "<Node L>"
            , "<Node M>"]
        nodes_str = [str(node) for node in deep[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_M_to_F_branch_and_bound(self):
        branch_and_bound = search.branch_and_bound_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound[1], 36, "It should have generated 36 nodes")
        self.assertEqual(branch_and_bound[2], 27, "It should have visited 27 nodes")
        self.assertEqual(branch_and_bound[3], 520, "The total cost is 520")

        route = ["<Node F>", "<Node S>", "<Node R>", "<Node C>", "<Node D>", "<Node M>"]
        nodes_str = [str(node) for node in branch_and_bound[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_M_to_F_branch_and_bound_h(self):
        branch_and_bound_with_h = search.branch_and_bound_with_heuristic_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound_with_h[1], 25, "It should have generated 25 nodes")
        self.assertEqual(branch_and_bound_with_h[2], 16, "It should have visited 16 nodes")
        self.assertEqual(branch_and_bound_with_h[3], 520, "The total cost is 520")

        route = ["<Node F>", "<Node S>", "<Node R>", "<Node C>", "<Node D>", "<Node M>"]
        nodes_str = [str(node) for node in branch_and_bound_with_h[0].path()]
        self.assertListEqual(route, nodes_str)


if __name__ == '__main__':
    unittest.main()