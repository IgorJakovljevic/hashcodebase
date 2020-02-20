class StreamHandler():
    def open(self, file_path):
        with open(file_path, "r") as f:
            first_line = f.readline().strip()
            number_of_books, number_of_libraries, number_of_days = map(int, first_line.split(" "))
            library_scores = dict()
            second_line = f.readline().strip()

            book_scores = list(map(int ,second_line.split(" ")))
            libraries = []

            first_line = f.readline().strip()
            second_line = f.readline().strip()


            while(len(first_line.split(" ")) > 0):

                books, signup, ship_time  = map(int, first_line.split(" "))
                lib = Library(books, signup, ship_time)

                lib.book_objects = list(map(int,second_line.split(" ")))
                libraries.append(lib)
                first_line = f.readline().strip()
                fl = first_line
                if(fl.replace(' ', '') == ""):
                    break

                second_line = f.readline().strip()
                if(second_line == ""):
                    break

            return Libraries(libraries, number_of_books, number_of_days)


    def write(self, file_path, write_objects):
        with open(file_path, "w") as f:
            for write_object in write_objects:
                f.write(str(write_object[0]) + "\n")
                f.write(" ".join(map(str, write_object[1])))

class StreamHandler2019():
    def open(self, file_path):
        with open(file_path, "r") as f:
            first_line = f.readline().strip()
            slices_to_order, types_of_pizza = map(int, first_line.split(" "))
            second_line = f.readline().strip()
            number_of_slices = list(map(int, second_line.split(" ")))

        # BUILDING DATA STRUCTURES
        slice_lookup = {i: x for i, x in enumerate(number_of_slices)}
        result = dict()
        result["slices_to_order"] = slices_to_order
        result["types_of_pizza"] = types_of_pizza
        result["number_of_slices"] = number_of_slices
        result["slice_lookup"] = slice_lookup
        return result

    def write(self, file_path, write_object):
        with open(file_path, "w") as f:
            f.write(str(len(write_object)) + "\n")
            f.write(" ".join(map(str, write_object)))