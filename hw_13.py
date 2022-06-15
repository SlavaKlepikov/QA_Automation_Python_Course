"""
Find web page.
Write 30 XPATH locators for this page using XPath Axes and Wildcards.
Some of them should have more than 3 steps.
For 10 XPATH locators write 10 CSS locators which find same element
"""

web_page = "https://ithillel.ua/"

"""
#id:
xpath: //button[@id = "btn-consultation-hero"]
css: btn-consultation-hero

#class:
xpath: //p[@class="footer-contacts-item_group"]
css: .footer-contacts-item_group

#child:
xpath: //ul[@id= "accordion-faq"]/child::*
css: ul[id= "accordion-faq"]>*

#and:
xpath: //img[@alt ="Ciklum" and @class ="company-symbol_img lozad"]
css: img[alt ="Ciklum"][class ="company-symbol_img lozad"]

#last and not:
xpath: //div[@class="swiper-slider_pagination-container"]//child::span[@class ="swiper-pagination-bullet" and not(@style) ][last()]

#parent:
xpath: //div[@class= "swiper-slide-row"]/parent::div[@class = "swiper-slide swiper-slide-active"]
xpath: //span[@class="swiper-pagination-bullet" and not(@style)]/parent::div
xpath: //li[@class="socials-list_item"]/parent::ul

#preceding-sibling
xpath: //span[@class="header-bar-link_text"]/preceding-sibling::*
xpath: //a[@data-city-id="od"]/preceding-sibling::a

#following-sibling:
xpath: //a[@data-city-id="online"]/following-sibling::span
css: a[data-city-id="online"]+span
xpath: //div[@id="swiper-coaches"]/child::div[@class="swiper-wrapper"]/following-sibling::div
css: div[id="swiper-coaches"] > div[class="swiper-wrapper"] + div

#following:
xpath: //span[@class="extra-links_copyright"]/following::button

#text:
xpath: //*[text() = 'Курси інтернет-маркетингу, SMM.']

#or:
xpath: //img[@width or @height]
css: img[width], img[height]

#contains:
xpath: //button[@class="site-nav-link" and contains(text(),"Школа")]
xpath: //button[contains(@class, "dropdown")]
css: button[class*="dropdown"]

#descendant:
xpath: //div[@class= "container"]/descendant::img[@alt="hammer"]

#ancestor:
xpath: //a[@href = "https://blog.ithillel.ua/articles/prioritization-in-testing"]/ancestor::section
xpath: ///button[@type ="submit"]/ancestor::footer[@class="site-footer"]
xpath: //*[local-name() = 'svg'][@id!= "ic_send"]/ancestor::button

#//@:
xpath: //@href

xpath: //img[@data-loaded]
css: img[data-loaded]

#local-name() and !=:
xpath: //*[local-name() = 'svg'][@fill != "none"]

#<:
xpath: //*[local-name() = 'svg'][@height < 9]

#ancestor-or-self:
xpath: //div[@class ="accordion_card-header" ]/ancestor-or-self::div

#concat:
xpath: //p[contains(text(), concat('2-й',' ', 'поверx'))]

#string-length:
xpath: //*[string-length(p[text()])>450]

#starts-with:
xpath: //a[starts-with(text(), 'Договір')]

#child and last()-1:
xpath: //ul[@id="accordion-faq"]/child::li[last()-1]
css: ul[id="accordion-faq"] li:last-child
xpath: //ul[@class= "course-nav_list"]//child::span[text() = 'advanced']
"""