<?xml version="1.0" encoding="UTF-8"?>

<callGraph>

<version>2</version>

<modules>

<module>

<id>0</id>

<name>D:\Users\boe\Documents\BoE\git\ewarm\callgraph\arm9202\Debug\Obj\cgt.o</name>

</module>

<module>

<id>1</id>

<name>D:\Users\boe\Documents\BoE\git\ewarm\callgraph\arm9202\Debug\Obj\main.o</name>

</module>

<module>

<id>2</id>

<name>cstartup\_M.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>3</id>

<name>cmain.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>4</id>

<name>vector\_table\_M.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>5</id>

<name>low\_level\_init.o</name>

<library>dl7M\_tln.a</library>

</module>

<module>

<id>6</id>

<name>exit.o</name>

<library>dl7M\_tln.a</library>

</module>

<module>

<id>7</id>

<name>vectortrap\_M.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>8</id>

<name>cexit.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>9</id>

<name>exit.o</name>

<library>shb\_l.a</library>

</module>

<module>

<id>10</id>

<name>data\_init.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>11</id>

<name>zero\_init3.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>12</id>

<name>copy\_init3.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>13</id>

<name>rle\_init\_single.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>14</id>

<name>rle\_init.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>15</id>

<name>packbits\_init\_single.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>16</id>

<name>packbits\_init.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>17</id>

<name>lz77\_init\_single.o</name>

<library>rt7M\_tl.a</library>

</module>

<module>

<id>18</id>

<name>lz77\_init.o</name>

<library>rt7M\_tl.a</library>

</module>

</modules>

<functions>

<function>

<id>0</id>

<name>cgt1</name>

<address>0x800&apos;00fd</address>

<stack>8</stack>

<callee>1</callee>

</function>

<function>

<id>1</id>

<name>cgt2</name>

<address>0x800&apos;0111</address>

<stack>0</stack>

</function>

<function>

<id>2</id>

<name>main</name>

<address>0x800&apos;00ef</address>

<stack>8</stack>

<callee>0</callee>

</function>

<function>

<id>3</id>

<name>\_\_iar\_program\_start</name>

<root>Program entry</root>

<address>0x800&apos;0135</address>

<stack>0</stack>

<callee>4</callee>

</function>

<function>

<id>4</id>

<name>\_\_cmain</name>

<address>0x800&apos;00cd</address>

<stack>0</stack>

<callee>2</callee>

<callee>5</callee>

<callee>6</callee>

<callee>10</callee>

</function>

<function>

<id>5</id>

<name>\_\_low\_level\_init</name>

<address>0x800&apos;00eb</address>

<stack>0</stack>

</function>

<function>

<id>6</id>

<name>exit</name>

<address>0x800&apos;00f9</address>

<stack>0</stack>

<callee>8</callee>

</function>

<function>

<id>7</id>

<name>\_\_default\_handler</name>

<localIn>7</localIn>

<root>interrupt</root>

<address>0x800&apos;006b</address>

<stack>0</stack>

</function>

<function>

<id>8</id>

<name>\_exit</name>

<address>0x800&apos;0115</address>

<stack>0</stack>

<callee>9</callee>

</function>

<function>

<id>9</id>

<name>\_\_exit</name>

<address>0x800&apos;0121</address>

<stack>8</stack>

</function>

<function>

<id>10</id>

<name>\_\_iar\_data\_init3</name>

<address>0x800&apos;006d</address>

<stack>8</stack>

<callee>11</callee>

</function>

<function>

<id>11</id>

<name>\_\_iar\_copy\_init3</name>

<address>0x800&apos;0041</address>

<stack>0</stack>

</function>

</functions>

<maxCallChains>

<maxCallChain>

<top>3</top>

<stack>16</stack>

<entry>

<function>3</function>

<stack>0</stack>

</entry>

<entry>

<function>4</function>

<stack>0</stack>

</entry>

<entry>

<function>2</function>

<stack>8</stack>

</entry>

<entry>

<function>0</function>

<stack>8</stack>

</entry>

<entry>

<function>1</function>

<stack>0</stack>

</entry>

</maxCallChain>

<maxCallChain>

<top>7</top>

<stack>0</stack>

<entry>

<function>7</function>

<stack>0</stack>

</entry>

</maxCallChain>

</maxCallChains>

</callGraph>
