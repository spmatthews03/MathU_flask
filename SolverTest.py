import unittest
from AlgebraProblem import AlgebraProblem
import algebra_helper
from Chatbot.Chatbot import ChatBot
class SolverTest(unittest.TestCase):
    def test_check_solve_for_x(self):
        prob = AlgebraProblem('2x+5-3y+3x','solve')
        self.assertEqual('5.0x+5.0-3.0y', algebra_helper.do_problem(prob))

    def test_check_solve_for_x_mult_negatives(self):
        prob = AlgebraProblem('2x+5-3y-10', 'solve')
        self.assertEqual('2.0x-5.0-3.0y', algebra_helper.do_problem(prob))

    def test_getting_vars_on_same_side(self):
        prob = AlgebraProblem('4x + 5y +1 = -3y +2x -3', 'solve')
        self.assertEqual('4x-2x+4=-8y', algebra_helper.get_variables_on_same_side(prob))

    def test_switching_sides1(self):
        prob = AlgebraProblem('4x+5y=6x-7y','solve')
        terms = algebra_helper.get_terms(prob.get_expression())
        term = '6x'
        self.assertEqual(['-6x','4x','+','5y','=','-7y'], algebra_helper.switch_sides(term, terms))


    def test_extract_problem1(self):
        sentence = 'Can you help me with 2x+5y= - 4 y'
        cb = ChatBot()
        self.assertEqual('2x+5y=-4y', cb.extract_problem(sentence))


    # def test_combine_like_terms1(self):
    #     terms = ['5x', '10x', '-8y', '4y','3','5','-7']
    #     self.assertEqual({'':1.0, 'x':15.0,'y':-4.0}, algebra_helper.combine_like_terms(terms))
    #
    # def test_combine_like_terms2(self):
    #     terms = ['15','-x','y','-x','5x','-7y']
    #     self.assertEqual({'':15.0, 'x':3.0,'y':-6.0}, algebra_helper.combine_like_terms(terms))

if __name__ == '__main__':
    unittest.main()
