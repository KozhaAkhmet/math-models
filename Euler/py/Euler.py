
def euler(y_der,a,b,t0,y0,h):
   M = int((b - a)/h)
   y_arr = [y0 + h*(y_der(t0,y0))]
   for i in range(1,M):
      y_arr.append(y_arr[i-1] + h*(y_der(i,y_arr[i-1])))

   print("\nH is: " + str(h))
   for i in range(len(y_arr)):
      print(str(i) + " " + str(y_arr[i]))

