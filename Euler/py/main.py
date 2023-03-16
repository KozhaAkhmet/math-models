import Euler

def main():
   def y_der(t,y):
      return (t - y)/2
   
   Euler.euler(y_der,0,3,0,1,1)
   Euler.euler(y_der,0,3,0,1,1/2)
   Euler.euler(y_der,0,3,0,1,1/4)
   Euler.euler(y_der,0,3,0,1,1/8)

if __name__ == '__main__':
   main()

"""
Output:
H is: 1
0 0.5
1 0.75
2 1.375

H is: 0.5
0 0.75
1 0.8125
2 1.109375
3 1.58203125
4 2.1865234375
5 2.889892578125

H is: 0.25
0 0.875
1 0.890625
2 1.029296875
3 1.275634765625
4 1.616180419921875
5 2.0391578674316406
6 2.5342631340026855
7 3.09248024225235
8 3.705920211970806
9 4.367680185474455
10 5.071720162290148
11 5.81275514200388

H is: 0.125
0 0.9375
1 0.94140625
2 1.007568359375
3 1.1320953369140625
4 1.3113393783569336
5 1.5418806672096252
6 1.8205131255090237
7 2.1442310551647097
8 2.5102166142169153
9 2.915828075828358
10 3.3585888210890857
11 3.836177019771018
12 4.3464159560353295
13 4.887264958783121
14 5.456810898859176
15 6.053260217680478
16 6.674931454075448
17 7.320248238195733
18 7.9877327233085
19 8.675999428101719
20 9.383749463845362
21 10.109765122355027
22 10.852904802207838
23 11.612098252069849

"""