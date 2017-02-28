from lxml import etree
test='''<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
         <br>
     </ul>
 </div>
'''
html=etree.HTML(test)
result1=html.xpath('//li/a/text()')
print(result1)
result=etree.tostring(html)

print(result)
