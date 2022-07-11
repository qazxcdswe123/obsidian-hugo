#Programming/Misc 

Every stream in C++ is tied to an output stream, which can be `null`.

What does this mean? First of all, it's important to understand that when you write `std::cout << "asdf"`, it is not necessarily immediately printed on the screen. It turns out that it is much better (in terms of performance) to collect it into a _buffer_ and then, at some point, _flush_ the buffer — i.e. empty its contents to the screen (or file, or any other "device"), all at once.

> By default, the standard narrow streams `cin` and `cerr` are tied to `cout`

In general I think people should read the documentation for such things instead of just pasting them "because it makes input faster".