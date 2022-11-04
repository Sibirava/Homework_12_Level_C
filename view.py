import Vector
import Task01
import Task02

def main():

    vector = Vector.random_vector_elements()

    avg = Task01.avg_vector(vector)

    hvg = Task02.hvg_vector(vector)

    d_discrepancy = int(input("Input the +- discrepancy: "))

    msg = (f"In {vector}: \n"
           f"1)There are {Task01.find_elements_vector_above_avg(vector,avg)} elements ABOVE "
           f"and {Task01.find_elements_vector_below_avg(vector,avg)} elements BELOW avg {avg} \n"
           f"2)There are {Task02.find_elements_vector_above_avg(vector,hvg)} elements ABOVE "
           f"and {Task02.find_elements_vector_below_avg(vector,hvg)} elements BELOW hvg {hvg} \n"
           f"3)Nearest numbers to avg {avg} +- discrepancy {d_discrepancy} "
           f"are in range {avg - d_discrepancy, avg + d_discrepancy} and are "
           f"{Task01.find_nearest_element_to_avg(vector, d_discrepancy, avg)} \n"
           f"3)Nearest numbers to hvg {hvg} +- discrepancy {d_discrepancy} "
           f"are in range {hvg - d_discrepancy, hvg + d_discrepancy} and are "
           f"{Task02.find_nearest_element_to_hvg(vector, d_discrepancy, hvg)}")

    print(msg)

main()