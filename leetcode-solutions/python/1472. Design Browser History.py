# https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_page_index = 0

    def visit(self, url: str) -> None:
        self.history = self.history[0:self.cur_page_index+1]
        self.history.append(url)
        self.cur_page_index += 1

    def back(self, steps: int) -> str:
        self.cur_page_index -= steps
        self.cur_page_index = max(self.cur_page_index, 0)
        return self.history[self.cur_page_index]
            
    def forward(self, steps: int) -> str:
        self.cur_page_index = min(self.cur_page_index + steps, len(self.history) - 1)
        return self.history[self.cur_page_index]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
