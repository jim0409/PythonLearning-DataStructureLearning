import sys


iter_num = 0


class init_node:
    """
    這邊初始化時定義了
    num並限制能放入的為數字
    salary並限制能放入的為數字
    name並限制能放入的為字串
    next不作限制，不過預計會放入下一個node
    """

    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None


def build_new_node(node_name, node_salary):
    global iter_num
    iter_num = iter_num + 1
    n = init_node()
    n.num = iter_num
    n.name = node_name
    n.salary = node_salary
    n.next = None

    return n


def dump_nodes(nodes):
    print_nodes = True
    while print_nodes:
        if nodes.next is None:
            print_nodes = False

        print("the nodes_{} include name: {} with salary: {}".format(
            nodes.num, nodes.name, nodes.salary))
        nodes = nodes.next


if __name__ == "__main__":
    data = [['jim', 100], ['tim', 200], ['kit', 300]]

    # 需要先宣告一個head來做node的初始化
    head = init_node()

    # 一定要，額外宣告一個ptr用來做迭代器的開頭
    ptr = head
    for i in data:
        newnode = build_new_node(i[0], i[1])
        ptr.next = newnode
        ptr = ptr.next

    dump_nodes(head)
