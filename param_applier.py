
class_name = "LFUCache"
methods = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
argss = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

solution_obj = None
for method, args in zip(methods, argss):
    if method == class_name:
        solution_obj = eval(f"{method}({','.join(str(arg) for arg in args)})")
    else:
        eval(f"solution_obj.{method}({','.join(str(arg) for arg in args)})")