KEY-FEATURES OF THE APPLICATION:
1) This Application is GUI based developed on Python 3.7+ 
2) Required: any Compiler of python and libraries like Tkinter and Matplotlib
3) This Data base has no limits on data-entries 
4) Data will be saved in form of .txt (more compatible)
5) The Graph Analysis 📈 is runtime analysis which makes it more user friendly
6) The Data Entries and Data is displayed dynamically.

GRAPHICAL DATA📊:

Functions used:
• Placing Graphs:
  o Shows Bar Graphs and can be line a graph by changing plt.bar to plt.line
• Insurance Analysis:
  o This profit-based system multiplies for 12 months of 10% and can be redo line103 
y = amount * 0.1 * 12

For Developers💻:
Back-End Functions

There is total 9 functions called at various places
1. delete_it
2. save_file
3. Show
4. Search
5. append_data
6. load_file
7. insurance_analysis
8. placing_graph
9. button_graph
The Data is saved as after every entry there is Seperator ‘,’ which separate the data of 
individual person data and each person's data is saved in next line.
The load_file function read data in ‘,’ format convert it into list 2-d and show them in list box 
display. save_file will fetch all the data from the list box and Save them into .txt file the list 
box return data in form of tuples but is converted into list and save in .txt in required formats.

Drawbacks:
• Shows Graph but year and planned years are not saved because time shortage can be done on need-base.
• Amount should contain only integer not alphabets otherwise graph will not be shown.
• Data is saved in organized form don’t misplace any data in .txt file
• File should be in .txt format
