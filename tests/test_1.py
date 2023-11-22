import unittest
import search


class MyTestCaseForAtoB(unittest.TestCase):

    def setUp(self):
        starting_city = 'A'
        goal_city = 'B'
        self.problem_to_resolve = search.GPSProblem(starting_city, goal_city, search.romania)

    def test_going_from_A_to_B_breath_first(self):
        broad = search.breadth_first_graph_search(self.problem_to_resolve)

        self.assertEqual(broad[1], 21, "It should have generated 21 nodes")
        self.assertEqual(broad[2], 16, "It should have visited 16 nodes")
        self.assertEqual(broad[3], 450, "The total cost is 450")

        route = ["<Node B>", "<Node F>", "<Node S>", "<Node A>"]
        nodes_str = [str(node) for node in broad[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_A_to_B_deep_first(self):
        deep = search.depth_first_graph_search(self.problem_to_resolve)
        self.assertEqual(deep[1], 18, "It should have generated 18 nodes")
        self.assertEqual(deep[2], 10, "It should have visited 10 nodes")
        self.assertEqual(deep[3], 733, "The total cost is 733")

        route = ["<Node B>", "<Node P>", "<Node C>", "<Node D>", "<Node M>", "<Node L>", "<Node T>", "<Node A>"]
        nodes_str = [str(node) for node in deep[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_A_to_B_branch_and_bound(self):
        branch_and_bound = search.branch_and_bound_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound[1], 31, "It should have generated 31 nodes")
        self.assertEqual(branch_and_bound[2], 24, "It should have visited 24 nodes")
        self.assertEqual(branch_and_bound[3], 418, "The total cost is 418")

        route = ["<Node B>", "<Node P>", "<Node R>", "<Node S>", "<Node A>"]
        nodes_str = [str(node) for node in branch_and_bound[0].path()]
        self.assertListEqual(route, nodes_str)

    def test_going_from_A_to_B_branch_and_bound_h(self):
        branch_and_bound_with_h = search.branch_and_bound_with_heuristic_search(self.problem_to_resolve)
        self.assertEqual(branch_and_bound_with_h[1], 16, "It should have generated 16 nodes")
        self.assertEqual(branch_and_bound_with_h[2], 6, "It should have visited 6 nodes")
        self.assertEqual(branch_and_bound_with_h[3], 418, "The total cost is 418")

        route = ["<Node B>", "<Node P>", "<Node R>", "<Node S>", "<Node A>"]
        nodes_str = [str(node) for node in branch_and_bound_with_h[0].path()]
        self.assertListEqual(route, nodes_str)


if __name__ == '__main__':
    unittest.main()