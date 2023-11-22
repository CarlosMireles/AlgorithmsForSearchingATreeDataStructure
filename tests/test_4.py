import unittest
import search


class MyTestCaseForNtoD(unittest.TestCase):

    def setUp(self):
        starting_city = 'N'
        goal_city = 'D'
        self.problem_to_resolve = search.GPSProblem(starting_city, goal_city, search.romania)

    def test_going_from_N_to_D_breath_first(self):
        broad = search.breadth_first_graph_search(self.problem_to_resolve)

        self.assertEqual(broad[1], 32, "It should have generated 32 nodes")
        self.assertEqual(broad[2], 26, "It should have visited 26 nodes")
        self.assertEqual(broad[3], 765, "The total cost is 765")

        route = ["<Node D>", "<Node C>", "<Node P>", "<Node B>", "<Node U>", "<Node V>", "<Node I>", "<Node N>"]
        nodes_str = [str(node) for node in broad[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_N_to_D_deep_first(self):
        deep = search.depth_first_graph_search(self.problem_to_resolve)
        self.assertEqual(deep[1], 31, "It should have generated 31 nodes")
        self.assertEqual(deep[2], 19, "It should have visited 19 nodes")
        self.assertEqual(deep[3], 1151, "The total cost is 1151")

        route = ["<Node D>", "<Node C>", "<Node P>", "<Node R>", "<Node S>", "<Node F>", "<Node B>", "<Node U>"
            , "<Node V>", "<Node I>", "<Node N>"]
        nodes_str = [str(node) for node in deep[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_N_to_D_branch_and_bound(self):
        branch_and_bound = search.branch_and_bound_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound[1], 32, "It should have generated 32 nodes")
        self.assertEqual(branch_and_bound[2], 26, "It should have visited 26 nodes")
        self.assertEqual(branch_and_bound[3], 765, "The total cost is 765")

        route = ["<Node D>", "<Node C>", "<Node P>", "<Node B>", "<Node U>", "<Node V>", "<Node I>", "<Node N>"]
        nodes_str = [str(node) for node in branch_and_bound[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_N_to_D_branch_and_bound_h(self):
        branch_and_bound_with_h = search.branch_and_bound_with_heuristic_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound_with_h[1], 23, "It should have generated 23 nodes")
        self.assertEqual(branch_and_bound_with_h[2], 12, "It should have visited 12 nodes")
        self.assertEqual(branch_and_bound_with_h[3], 765, "The total cost is 765")

        route = ["<Node D>", "<Node C>", "<Node P>", "<Node B>", "<Node U>", "<Node V>", "<Node I>", "<Node N>"]
        nodes_str = [str(node) for node in branch_and_bound_with_h[0].path()]
        self.assertListEqual(route, nodes_str)


if __name__ == '__main__':
    unittest.main()