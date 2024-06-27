from typing import Optional
from math import ceil


class Pagination:
    def __init__(self, items: Optional[list] = None, page_size: int = 10) -> None:
        self.items = items
        self.page_size = page_size
        self.current_page = 1
        self.total_pages = ceil(len(items) // page_size)  # // - divides and floors

    def prevPage(self):
        self.goToPage(self.current_page - 1)

    def nextPage(self):
        self.goToPage(self.current_page + 1)

    def firstPage(self):
        self.goToPage(1)

    def lastPage(self):
        self.goToPage(self.total_pages)

    def goToPage(self, page_num: int):
        if page_num <= 0 or page_num > self.total_pages:
            raise ValueError(
                "page_num isn't in the correct range of the available pages"
            )
        self.current_page = page_num

    def get_visible_items(self) -> list:
        end_idx = self.current_page * self.page_size  # 2 * 4 -> 8
        start_idx = end_idx - self.page_size  # 8 - 4 = 4
        return self.items[start_idx:end_idx]


def main():
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    p.goToPage(1)
    p.lastPage()
    current_items = p.get_visible_items()
    print(current_items)


if __name__ == "__main__":
    main()
