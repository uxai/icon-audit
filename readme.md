# Icon mapping

This was a simple tool that was created to map icon names with what existed in design systems. It was fairly primitive since our first initiative was to create an excel sheet that contained all the names of the design systems icons and all the names of what existed in Web (if at all).

Afterwards, we needed a way to map what was being said in design systems to web, and ensure that the old icon names were being translated properly.

```
[prefix]-iconname-##-[fit]-[colored]
```

Our new naming convention was as follows:
```
prefix - platform specific prefix for reference	
##	- Associated height for the icon		
fit	- means this icon fills the entire container		
colored	- means the icon is already colored and should never be altered	
```

This tool would output a new CSV that showed what icons were in design systems, the sizes available, and how the name should appear in the specified platform, all while showing what the old name was in the first column to map properly.

This tool is quite specific to the data we had at hand, I am putting it here just as my own record and reference. If somehow you do feel it is useful, feel free to use it as needed or modify to be more 'global'
