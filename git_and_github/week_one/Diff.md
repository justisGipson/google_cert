### diff

diff is used to find differences between two files. On its own, it’s a bit hard to use; instead, use it with diff -u to find lines which differ in two files:

### diff -u

diff -u is used to compare two files, line by line, and have the differing lines compared side-by-side in the same output. See below:

``` {contenteditable="false" data-language="python" style="opacity: 1"}
123456789101112131415161718192021222324252627282930~$ cat menu1.txt Menu1: ApplesBananasOrangesPears ~$ cat menu2.txt Menu: ApplesBananasGrapesStrawberries ~$ diff -u menu1.txt menu2.txt --- menu1.txt   2019-12-16 18:46:13.794879924 +0900+++ menu2.txt   2019-12-16 18:46:42.090995670 +0900@@ -1,6 +1,6 @@-Menu1:+Menu:  Apples Bananas-Oranges-Pears+Grapes+Strawberries Enter to Rename, ⇧Enter to Preview.monaco-list.list_id_1:focus .monaco-list-row.focused { background-color: #d6ebff; }
.monaco-list.list_id_1:focus .monaco-list-row.focused:hover { background-color: #d6ebff; }
.monaco-list.list_id_1:focus .monaco-list-row.selected { background-color: #0069d1; }
.monaco-list.list_id_1:focus .monaco-list-row.selected:hover { background-color: #0069d1; }
.monaco-list.list_id_1:focus .monaco-list-row.selected { color: #ffffff; }

                .monaco-drag-image,
                .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { background-color: #0074e8; }
            

                .monaco-drag-image,
                .monaco-list.list_id_1:focus .monaco-list-row.selected.focused { color: #ffffff; }
            
.monaco-list.list_id_1 .monaco-list-row.focused { background-color:  #d6ebff; }
.monaco-list.list_id_1 .monaco-list-row.focused:hover { background-color:  #d6ebff; }
.monaco-list.list_id_1 .monaco-list-row.selected { background-color:  #e4e6f1; }
.monaco-list.list_id_1 .monaco-list-row.selected:hover { background-color:  #e4e6f1; }
.monaco-list.list_id_1:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color:  #f0f0f0; }

                .monaco-list.list_id_1.drop-target,
                .monaco-list.list_id_1 .monaco-list-rows.drop-target,
                .monaco-list.list_id_1 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; }
            
.monaco-list-type-filter { background-color: #efc1ad }
.monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); }
.monaco-list-type-filter.no-matches { border: 1px solid #be1100; }
.monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }
```

### Patch

Patch is useful for applying file differences. See the below example, which compares two files. The comparison is saved as a .diff file, which is then patched to the original file!

``` {contenteditable="false" data-language="python" style="opacity: 1"}
123456789101112131415161718192021~$ cat hello_world.txt Hello World~$ cat hello_world_long.txt Hello World It's a wonderful day!~$ diff -u hello_world.txt hello_world_long.txt --- hello_world.txt     2019-12-16 19:24:12.556102821 +0900+++ hello_world_long.txt        2019-12-16 19:24:38.944207773 +0900@@ -1 +1,3 @@ Hello World++It's a wonderful day!~$ diff -u hello_world.txt hello_world_long.txt > hello_world.diff~$ patch < hello_world.diff patching file hello_world.txt~$ cat hello_world.txt Hello World It's a wonderful day! Enter to Rename, ⇧Enter to Preview.monaco-list.list_id_2:focus .monaco-list-row.focused { background-color: #d6ebff; }
.monaco-list.list_id_2:focus .monaco-list-row.focused:hover { background-color: #d6ebff; }
.monaco-list.list_id_2:focus .monaco-list-row.selected { background-color: #0069d1; }
.monaco-list.list_id_2:focus .monaco-list-row.selected:hover { background-color: #0069d1; }
.monaco-list.list_id_2:focus .monaco-list-row.selected { color: #ffffff; }

                .monaco-drag-image,
                .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { background-color: #0074e8; }
            

                .monaco-drag-image,
                .monaco-list.list_id_2:focus .monaco-list-row.selected.focused { color: #ffffff; }
            
.monaco-list.list_id_2 .monaco-list-row.focused { background-color:  #d6ebff; }
.monaco-list.list_id_2 .monaco-list-row.focused:hover { background-color:  #d6ebff; }
.monaco-list.list_id_2 .monaco-list-row.selected { background-color:  #e4e6f1; }
.monaco-list.list_id_2 .monaco-list-row.selected:hover { background-color:  #e4e6f1; }
.monaco-list.list_id_2:not(.drop-target) .monaco-list-row:hover:not(.selected):not(.focused) { background-color:  #f0f0f0; }

                .monaco-list.list_id_2.drop-target,
                .monaco-list.list_id_2 .monaco-list-rows.drop-target,
                .monaco-list.list_id_2 .monaco-list-row.drop-target { background-color: #d6ebff !important; color: inherit !important; }
            
.monaco-list-type-filter { background-color: #efc1ad }
.monaco-list-type-filter { border: 1px solid rgba(0, 0, 0, 0); }
.monaco-list-type-filter.no-matches { border: 1px solid #be1100; }
.monaco-list-type-filter { box-shadow: 1px 1px 1px #a8a8a8; }
```

There are some other interesting patch and diff commands such as patch -p1, diff -r !

Check them out in the following references:

-   [http://man7.org/linux/man-pages/man1/diff.1.html](http://man7.org/linux/man-pages/man1/diff.1.html)
-   [http://man7.org/linux/man-pages/man1/patch.1.html](http://man7.org/linux/man-pages/man1/patch.1.html)
