
[GFG](https://www.geeksforgeeks.org/file-handling-c-classes/)

> • istream (input stream) type, which provides input operations
> • ostream (output stream) type, which provides output operations
> • cin, an istream object that reads the standard input
> • cout, an ostream object that writes to the standard output
> • cerr, an ostream object, typically used for program error messages, that writes to the standard error
> • The >> operator, which is used to read input from an istream object
> • The << operator, which is used to write output to an ostream object
> • The getline function (§ 3.2.2, p. 87), which reads a line of input from a given istream into a given string
> C++ Primer P310

| Mode Flag     | Description                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `ios::in`     | Open for input operations.                                                                                                   |
| `ios::out`    | Open for output operations.                                                                                                  |
| `ios::binary` | Open in binary mode.                                                                                                         |
| `ios::ate`    | Set the initial position at the end of the file. If this flag is not set, the initial position is the beginning of the file. |
| `ios::app`    | All output operations are performed at the end of the file, appending the content to the current content of the file.        |
| `ios::trunc`  | If the file is opened for output operations and it already existed, its previous content is deleted and replaced by the new one.                                                                                                                             |

| class    | default mode parameter |
| -------- | ---------------------- |
| ofstream | ios::out               |
| ifstream | ios::in                |
| fstream  | ios::in \| ios::out                       |

# Example
```cpp
// Open the file in read mode
ifstream myFile("myfile.txt");

// Check if the file was opened successfully
if (myFile.is_open()) {
  // Declare a string to hold each line of the file
  string line;

  // Read each line of the file until we reach the end
  while (getline(myFile, line)) {
    // Print the line to the console
    cout << line << endl;
  }

  // Close the file
  myFile.close();
} else {
  // Print an error message if the file could not be opened
  cout << "Error opening file!" << endl;
}
```