import xlwings as xw
import pandas as pd

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"

    df = pd.DataFrame(data=[['Alex', 10], ['Fred', 12], ['Dave', 13]], index=['a', 'b', 'c'], columns=['Name', 'Age'])

    sheet["A3"].value = df  # writes df to spreadsheet
    wb.sheets[0].range('F3').value = df  # same as above

@xw.func
def hello(name):
    return f"Hello {name}!"

@xw.func
def user_def_function():
    return 1

if __name__ == "__main__":
    xw.Book("pyxlwings.xlsm").set_mock_caller()
    main()
