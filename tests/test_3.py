import unittest
import search


class MyTestCaseForGtoZ(unittest.TestCase):

    def setUp(self):
        starting_city = 'G'
        goal_city = 'Z'
        self.problem_to_resolve = search.GPSProblem(starting_city, goal_city, search.romania)

    def test_going_from_G_to_Z_breath_first(self):
        broad = search.breadth_first_graph_search(self.problem_to_resolve)

        self.assertEqual(broad[1], 41, "It should have generated 41 nodes")
        self.assertEqual(broad[2], 34, "It should have visited 34 nodes")
        self.assertEqual(broad[3], 615, "The total cost is 615")

        route = ["<Node Z>", "<Node A>", "<Node S>", "<Node F>", "<Node B>", "<Node G>"]
        nodes_str = [str(node) for node in broad[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_G_to_Z_deep_first(self):
        deep = search.depth_first_graph_search(self.problem_to_resolve)
        self.assertEqual(deep[1], 32, "It should have generated 32 nodes")
        self.assertEqual(deep[2], 21, "It should have visited 21 nodes")
        self.assertEqual(deep[3], 1284, "The total cost is 1284")

        route = ["<Node Z>", "<Node A>", "<Node T>", "<Node L>", "<Node M>", "<Node D>", "<Node C>", "<Node P>"
            , "<Node R>", "<Node S>", "<Node F>", "<Node B>", "<Node G>"]
        nodes_str = [str(node) for node in deep[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_G_to_Z_branch_and_bound(self):
        branch_and_bound = search.branch_and_bound_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound[1], 41, "It should have generated 41 nodes")
        self.assertEqual(branch_and_bound[2], 35, "It should have visited 35 nodes")
        self.assertEqual(branch_and_bound[3], 583, "The total cost is 583")

        route = ["<Node Z>", "<Node A>", "<Node S>", "<Node R>", "<Node P>", "<Node B>", "<Node G>"]
        nodes_str = [str(node) for node in branch_and_bound[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_G_to_Z_branch_and_bound_h(self):
        branch_and_bound_with_h = search.branch_and_bound_with_heuristic_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound_with_h[1], 26, "It should have generated 26 nodes")
        self.assertEqual(branch_and_bound_with_h[2], 12, "It should have visited 12 nodes")
        self.assertEqual(branch_and_bound_with_h[3], 583, "The total cost is 583")

        route = ["<Node Z>", "<Node A>", "<Node S>", "<Node R>", "<Node P>", "<Node B>", "<Node G>"]
        nodes_str = [str(node) for node in branch_and_bound_with_h[0].path()]
        self.assertListEqual(route, nodes_str)


if __name__ == '__main__':
    unittest.main()