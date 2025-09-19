"""
3484. Design Spreadsheet
Level: Medium
Topics: Design, Hash Table, matrix
Link: https://leetcode.com/problems/design-spreadsheet?envType=daily-question&envId=2025-09-19
Time Complexity: O(1) for setCell and resetCell, O(m) for getValue where m is the length of the formula.
Space Complexity: O(n) where n is the number of cells set.
"""


class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadSheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.spreadSheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadSheet[cell] = 0

    def getValue(self, formula: str) -> int:
        operationIndex = formula.find('+')
        cell1 = formula[1:operationIndex]
        cell2 = formula[operationIndex + 1:]
        if cell1[0].isupper():
            num1 = self.spreadSheet.get(cell1, 0)
        else:
            num1 = int(cell1)
        if cell2[0].isupper():
            num2 = self.spreadSheet.get(cell2, 0)
        else:
            num2 = int(cell2)
        res = num1 + num2
        return res

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)