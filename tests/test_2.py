import unittest
import search


class MyTestCaseForOtoE(unittest.TestCase):

    def setUp(self):
        starting_city = 'O'
        goal_city = 'E'
        self.problem_to_resolve = search.GPSProblem(starting_city, goal_city, search.romania)

    def test_going_from_O_to_E_breath_first(self):
        broad = search.breadth_first_graph_search(self.problem_to_resolve)

        self.assertEqual(broad[1], 45, "It should have generated 45 nodes")
        self.assertEqual(broad[2], 43, "It should have visited 43 nodes")
        self.assertEqual(broad[3], 730, "The total cost is 730")

        route = ["<Node E>", "<Node H>", "<Node U>", "<Node B>", "<Node F>", "<Node S>", "<Node O>"]
        nodes_str = [str(node) for node in broad[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_O_to_E_deep_first(self):
        deep = search.depth_first_graph_search(self.problem_to_resolve)
        self.assertEqual(deep[1], 41, "It should have generated 41 nodes")
        self.assertEqual(deep[2], 31, "It should have visited 31 nodes")
        self.assertEqual(deep[3], 698, "The total cost is 698")

        route = ["<Node E>", "<Node H>", "<Node U>", "<Node B>", "<Node P>", "<Node R>", "<Node S>", "<Node O>"]
        nodes_str = [str(node) for node in deep[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_O_to_E_branch_and_bound(self):
        branch_and_bound = search.branch_and_bound_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound[1], 43, "It should have generated 43 nodes")
        self.assertEqual(branch_and_bound[2], 40, "It should have visited 40 nodes")
        self.assertEqual(branch_and_bound[3], 698, "The total cost is 698")

        route = ["<Node E>", "<Node H>", "<Node U>", "<Node B>", "<Node P>", "<Node R>", "<Node S>", "<Node O>"]
        nodes_str = [str(node) for node in branch_and_bound[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_O_to_E_branch_and_bound_h(self):
        branch_and_bound_with_h = search.branch_and_bound_with_heuristic_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound_with_h[1], 32, "It should have generated 32 nodes")
        self.assertEqual(branch_and_bound_with_h[2], 15, "It should have visited 15 nodes")
        self.assertEqual(branch_and_bound_with_h[3], 698, "The total cost is 698")

        route = ["<Node E>", "<Node H>", "<Node U>", "<Node B>", "<Node P>", "<Node R>", "<Node S>", "<Node O>"]
        nodes_str = [str(node) for node in branch_and_bound_with_h[0].path()]
        self.assertListEqual(route, nodes_str)


if __name__ == '__main__':
    unittest.main()