parsedom
=========

This is a fork of `Common Functions and ParseDOM <https://github.com/HenrikDK/xbmc-common-plugin-functions>`_ for use outside of XBMC.


Getting element content.
-------------------------

.. code:: python

    from parsedom import parseDOM
    link_html = "<a href='bla.html'>Link Test</a>"
    ret = parseDOM(link_html, "a")
    print repr(ret) # Prints ['Link Test']



Getting an element attribute.
-----------------------------

.. code:: python

    link_html = "<a href='bla.html'>Link Test</a>"
    ret = parseDOM(link_html, "a", ret = "href")
    print repr(ret) # Prints ['bla.html']


Get element with matching attribute.
---------------------------------------

.. code:: python

    link_html = "<a href='bla1.html' id='link1'>Link Test1</a><a href='bla2.html' id='link2'>Link Test2</a><a href='bla3.html' id='link3'>Link Test3</a>"
    ret1 = parseDOM(link_html, "a", attrs = { "id": "link1" }, ret = "href")
    ret2 = parseDOM(link_html, "a", attrs = { "id": "link2" })
    ret3 = parseDOM(link_html, "a", attrs = { "id": "link3" }, ret = "id")
    print repr(ret1) # Prints ['bla1.html']
    print repr(ret2) # Prints ['Link Test2']
    print repr(ret3) # Prints ['link3']

When scraping sites it is prudent to scrape in steps, since real websites are often complicated.

Take this example where you want to get all the user uploads.

.. code:: html

     &lt;div id="content"&gt;
      &lt;div id="sidebar"&gt;
       &lt;div id="latest"&gt;
        <a href="/video?8wxOVn99FTE">Miley Cyrus - When I Look At You</a>&gt;br /&lt;
        <a href="/video?46">Puppet theater</a>&lt;br /&gt;
        <a href="/video?98">VBLOG #42</a>&lt;br /&gt;
        <a href="/video?11">Fourth upload</a>&lt;br /&gt;
       &lt;/div&gt;
      &lt;/div&gt;
      &lt;div id="user"&gt;
       &lt;div id="uploads"&gt;
        <a href="/video?12">First upload</a>&lt;br /&gt;
        <a href="/video?23">Second upload</a>&lt;br /&gt;
        <a href="/video?34">Third upload</a>&lt;br /&gt;
        <a href="/video?41">Fourth upload</a>&lt;br /&gt;
       &lt;/div&gt;
      &lt;/div&gt;
     &lt;/div&gt;


The first step is to limit your search to the correct area.

One should always find the inner most DOM element that contains the needed data.

.. code:: python

    ret = parseDOM(html, "div", attrs = { "id": "uploads" })


The variable ret now contains

.. code:: python

    ['<a href="/video?12">First upload</a>&lt;br /&gt;
    <a href="/video?23">Second upload</a>&lt;br /&gt;
    <a href="/video?34">Third upload</a>&lt;br /&gt;
    <a href="/video?41">Fourth upload</a>&lt;br /&gt;']

And now we get the video url.

.. code:: python

    videos = parseDOM(ret, "a", ret = "href")
    print repr(videos) # Prints [ "video?12", "video?23", "video?34", "video?41" ]


