from points.points import Points


if __name__ == "__main__":
    try:
        p = Points(11, 10, may_exceed=True)
        p2 = Points(11, 79)
        print(f"{p != p2 = }")

    except Exception as error:
        print(error)
    else:
        print("No errors")
    ...
