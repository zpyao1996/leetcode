from collections import defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        reversed_equations = [[j, i] for [i, j] in equations]
        reversed_values = [1 / value for value in values]
        equations = equations + reversed_equations
        values = values + reversed_values
        equation_value_dict = defaultdict(dict)
        for equation, value in zip(equations, values):
            equation_value_dict[equation[0]][equation[1]] = value
        ans_list = []
        for query in queries:
            def get_query(query, equation_value_dict):
                start, end = query
                if start == end:
                    if start in equation_value_dict:
                        return 1.0
                    else:
                        return -1.0
                visited = set()
                node_val_stack = [(start, 1)]
                while node_val_stack:
                    node, val = node_val_stack.pop()
                    visited.add(node)
                    if node in equation_value_dict.keys():
                        for node2 in equation_value_dict[node].keys():
                            if node2 in visited:
                                continue
                            new_val = val * equation_value_dict[node][node2]
                            if node2 == end:
                                return float(new_val)
                            else:
                                node_val_stack.append([node2, new_val])
                return -1.0

            ans_list.append(get_query(query, equation_value_dict))
        return ans_list

