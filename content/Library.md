[c++ - When to use dynamic vs. static libraries - Stack Overflow](https://stackoverflow.com/questions/140061/when-to-use-dynamic-vs-static-libraries)
> Static libraries increase the size of the code in your binary. They're always loaded and whatever version of the code you compiled with is the version of the code that will run.
> 
> Dynamic libraries are stored and versioned separately. It's possible for a version of the dynamic library to be loaded that wasn't the original one that shipped with your code **if** the update is considered binary compatible with the original version.
> 
> Additionally dynamic libraries aren't necessarily loaded -- they're usually loaded when first called -- and can be shared among components that use the same library (multiple data loads, one code load).
> 
> Dynamic libraries were considered to be the better approach most of the time, but originally they had a major flaw (google DLL hell), which has all but been eliminated by more recent Windows OSes (Windows XP in particular).