from .LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):

    def __init__(self, token, left=None, right=None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self._add_root(token)
        if left is not None:
            if token not in "+-*/":
                raise ValueError("token must be valid operator")
            self._attach(self.root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return "".join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(p.element())
            return

        result.append("(")
        result.append(self._parenthesize_recur(self.left(p), result))

        result.append(p.element())

        result.append(self._parenthesize_recur(self.right(p), result))
        result.append(")")

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return p.element()
        else:
            left_result = self._evaluate_recur(self.left(p))
            right_result = self._evaluate_recur(self.right(p))
            operation = p.element()

            if operation == "+":
                return left_result + right_result
            elif operation == "-":
                return left_result - right_result
            elif operation == "*":
                return left_result * right_result
            else:
                return left_result / right_result




def build_exp_trees(tokens):
    S = []
    for token in tokens:
        if token not in "()":
            S.append(ExpressionTree(token))
        elif token in "+-*/":
            S.append(token)
        elif token == ")":
            right = S.pop()
            operator = S.pop()
            left = S.pop()
            S.append(ExpressionTree(operator, left, right))

    return S.pop()