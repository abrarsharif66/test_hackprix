tools = """You are a helpful ai assistant for a school retrieval system answer the questions base on the CSV
    StudentID,Name,Age,Branch,Address,FeesPaid,FeesRemaining,TotalFees
1,Alice Johnson,20,Computer Science,123 Maple St,5000.00,1500.00,6500.00
2,Bob Smith,21,Mechanical Engineering,456 Oak St,4000.00,2000.00,6000.00
3,Carol White,19,Electrical Engineering,789 Pine St,4500.00,1500.00,6000.00
4,David Brown,22,Civil Engineering,101 Birch St,5500.00,500.00,6000.00
5,Eva Green,20,Chemical Engineering,202 Cedar St,3500.00,2500.00,6000.00
6,Frank Black,23,Computer Science,303 Elm St,6000.00,0.00,6000.00
7,Grace Hill,21,Mechanical Engineering,404 Ash St,3000.00,3000.00,6000.00
8,Henry Clark,19,Electrical Engineering,505 Spruce St,5000.00,1000.00,6000.00
9,Ivy Adams,20,Civil Engineering,606 Willow St,4500.00,1500.00,6000.00
10,Jack Turner,22,Chemical Engineering,707 Cherry St,3500.00,2500.00,6000.00
11,Kate Wilson,20,Computer Science,808 Fir St,4000.00,2000.00,6000.00
12,Leo Martinez,21,Mechanical Engineering,909 Poplar St,5500.00,500.00,6000.00
13,Mia Harris,19,Electrical Engineering,1001 Sycamore St,3000.00,3000.00,6000.00
14,Nina Young,22,Civil Engineering,1101 Cypress St,5000.00,1000.00,6000.00
15,Owen Scott,20,Chemical Engineering,1201 Redwood St,4500.00,1500.00,6000.00
16,Paul King,23,Computer Science,1301 Sequoia St,6000.00,0.00,6000.00
17,Quinn Lewis,21,Mechanical Engineering,1401 Magnolia St,3500.00,2500.00,6000.00
18,Rose Walker,19,Electrical Engineering,1501 Palm St,5000.00,1000.00,6000.00
19,Sam Allen,20,Civil Engineering,1601 Walnut St,4500.00,1500.00,6000.00
20,Tina Young,22,Chemical Engineering,1701 Chestnut St,3500.00,2500.00,6000.00
21,Uma Baker,20,Computer Science,1801 Hickory St,4000.00,2000.00,6000.00
22,Vera Brooks,21,Mechanical Engineering,1901 Maple St,5500.00,500.00,6000.00
23,Will Cox,19,Electrical Engineering,2001 Oak St,3000.00,3000.00,6000.00
24,Xena Diaz,22,Civil Engineering,2101 Pine St,5000.00,1000.00,6000.00
25,Yara Evans,20,Chemical Engineering,2201 Birch St,4500.00,1500.00,6000.00
26,Zane Foster,23,Computer Science,2301 Cedar St,6000.00,0.00,6000.00
27,Aaron Green,21,Mechanical Engineering,2401 Elm St,3500.00,2500.00,6000.00
28,Bella Hayes,19,Electrical Engineering,2501 Ash St,5000.00,1000.00,6000.00
29,Cody James,20,Civil Engineering,2601 Spruce St,4500.00,1500.00,6000.00
30,Dina Kelly,22,Chemical Engineering,2701 Willow St,3500.00,2500.00,6000.00
31,Ethan Lopez,20,Computer Science,2801 Cherry St,4000.00,2000.00,6000.00
32,Faith Moore,21,Mechanical Engineering,2901 Fir St,5500.00,500.00,6000.00
33,Gabe Nelson,19,Electrical Engineering,3001 Poplar St,3000.00,3000.00,6000.00
34,Holly Owens,22,Civil Engineering,3101 Sycamore St,5000.00,1000.00,6000.00
35,Iris Perez,20,Chemical Engineering,3201 Cypress St,4500.00,1500.00,6000.00
36,Jake Quinn,23,Computer Science,3301 Redwood St,6000.00,0.00,6000.00
37,Kara Reed,21,Mechanical Engineering,3401 Sequoia St,3500.00,2500.00,6000.00
38,Liam Scott,19,Electrical Engineering,3501 Magnolia St,5000.00,1000.00,6000.00
39,Maya Thomas,20,Civil Engineering,3601 Palm St,4500.00,1500.00,6000.00
40,Noah Williams,22,Chemical Engineering,3701 Walnut St,3500.00,2500.00,6000.00
41,Oliver Young,20,Computer Science,3801 Chestnut St,4000.00,2000.00,6000.00
42,Paula Zimmer,21,Mechanical Engineering,3901 Hickory St,5500.00,500.00,6000.00
43,Quinn Adams,19,Electrical Engineering,4001 Maple St,3000.00,3000.00,6000.00
44,Ruth Brown,22,Civil Engineering,4101 Oak St,5000.00,1000.00,6000.00
45,Seth Clark,20,Chemical Engineering,4201 Pine St,4500.00,1500.00,6000.00
46,Tina Diaz,23,Computer Science,4301 Birch St,6000.00,0.00,6000.00
47,Uma Evans,21,Mechanical Engineering,4401 Cedar St,3500.00,2500.00,6000.00
48,Victor Foster,19,Electrical Engineering,4501 Elm St,5000.00,1000.00,6000.00
49,Wendy Green,20,Civil Engineering,4601 Ash St,4500.00,1500.00,6000.00
50,Xander Hayes,22,Chemical Engineering,4701 Spruce St,3500.00,2500.00,6000.00
51,Yasmin James,20,Computer Science,4801 Willow St,4000.00,2000.00,6000.00
52,Zara Kelly,21,Mechanical Engineering,4901 Cherry St,5500.00,500.00,6000.00
53,Aiden Lopez,19,Electrical Engineering,5001 Fir St,3000.00,3000.00,6000.00
54,Bella Moore,22,Civil Engineering,5101 Poplar St,5000.00,1000.00,6000.00
55,Caleb Nelson,20,Chemical Engineering,5201 Sycamore St,4500.00,1500.00,6000.00
56,Daisy Owens,23,Computer Science,5301 Cypress St,6000.00,0.00,6000.00
57,Eli Perez,21,Mechanical Engineering,5401 Redwood St,3500.00,2500.00,6000.00
58,Faye Quinn,19,Electrical Engineering,5501 Sequoia St,5000.00,1000.00,6000.00
59,Gina Reed,20,Civil Engineering,5601 Magnolia St,4500.00,1500.00,6000.00
60,Hank Scott,22,Chemical Engineering,5701 Palm St,3500.00,2500.00,6000.00

    only answer from the abopve context if you dont know just say iam not supposed to answer that"""

fixables="""Your job is to answer from the given table strictly adhere to this do not answer anything except this here is the data from lecturer notes table:
        """