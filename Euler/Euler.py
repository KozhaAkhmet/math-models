
def euler(y_der,a,b,t0,y0,h):
   M = int((b - a)/h)
   y_arr = [y0 + h*(y_der(t0,y0))]
   for i in range(1,M):
      y_arr.append(y_arr[i-1] + h*(y_der(i,y_arr[i-1])))

   print("\nH is: " + str(h))
   for i in range(len(y_arr)):
      print(str(i) + " " + str(y_arr[i]))


def main():
   def y_der(t,y):
      return (t - y)/2
   
   euler(y_der,0,3,0,1,1)
   euler(y_der,0,3,0,1,1/2)
   euler(y_der,0,3,0,1,1/4)
   euler(y_der,0,3,0,1,1/8)

if __name__ == '__main__':
   main()
