## DB File Structures
- Unordered Heap Files
	- Records placed arbitrarily across pages
	- [[Linked list]] or [[Page directory]]
- Clustered Heap Files
	- Records and pages are grouped
- Sorted Files
	- Pages and records are in sorted order
- Index Files
	- B+ Trees, Linear [[Hashing]], …
	- May contain records or point to records in other files

## Records
 - Fixed Length Records (FLR)
	- Unpacked: Use [[Bitmap]]
	- ![image.png](https://img.ynchen.me/2023/02/a714d215151eaa9d359f2bf095a1903f.webp)
	- ![image.png](https://img.ynchen.me/2023/02/80099c11c60a674a739a3326919f5590.webp)
	- ![image.png](https://img.ynchen.me/2023/02/85be9f76eba2bdafacb46c207d59576d.webp)
 - Variable Length Records (VLR)
	- Slotted Page
		- each page uses a page footer that maintains a slot directory tracking slot count, a free space pointer, and entries.
		- The slot count tracks the total number of slots. This includes both filled and empty slots. 
		- The free space pointer points to the next free position within the page.
		- Full when footer and records come together.
		- ![image.png](https://img.ynchen.me/2023/02/b199ff4a25ab7b5f3183594684cc904e.webp)