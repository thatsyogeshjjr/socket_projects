import curses


def generate_table_data():
    # Function to generate sample table data
    data = []
    for i in range(1, 51):
        data.append([f"Item {i}", f"Description of Item {i}", f"Price {i}"])
    return data


def main(stdscr):
    # Setup
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Generate sample table data
    table_data = generate_table_data()

    # Calculate window size based on the number of rows
    table_height = min(curses.LINES - 3, len(table_data) + 2)
    table_width = curses.COLS - 2

    # Create a window for the table
    table_win = curses.newwin(table_height, table_width, 1, 1)
    table_win.box()

    # Create a window for the header
    header_win = curses.newwin(1, curses.COLS, 0, 0)
    header_win.addstr(0, 2, "Crypto Data")
    header_win.refresh()

    # Display table data
    for i, row in enumerate(table_data):
        if i >= table_height - 2:
            break
        for j, col in enumerate(row):
            if j*20 + len(col) < table_width - 2:
                table_win.addstr(i+1, j*20+2, col)
    table_win.refresh()

    # Wait for user input
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break


curses.wrapper(main)
