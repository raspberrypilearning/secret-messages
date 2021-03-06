## अतिरिक्त कैरेक्टर्स

कुछ अक्षर वर्णमाला में नहीं हैं, जो त्रुटि का कारण बनता है।

+ कुछ ऐसे अक्षरों के साथ अपने कोड का परीक्षण करें जो वर्णमाला में नहीं हैं।
    
    उदाहरण के लिए, आप इस प्रकार के संदेश का उपयोग कर सकते हैं `hi there!!` ।
    
    ![स्क्रीनशॉट](images/messages-extra-characters.png)
    
    ध्यान दें कि स्पेस और `!`, सभी अक्षर 'c' के रूप में एन्क्रिप्टेड हैं!

+ इसे ठीक करने के लिए, आप केवल उस अक्षर का अनुवाद करना चाहते हैं जो वर्णमाला में है। ऐसा करने के लिए, अपने कोड में `if` स्टेटमेंट जोड़ें, और अपने बाकी कोड के इंडेंट करें।
    
    ![स्क्रीनशॉट](images/messages-if.png)

+ अपने कोड का परीक्षण पहले वाले ही संदेश के साथ करें। इस बार क्या होता है?
    
    ![स्क्रीनशॉट](images/messages-if-test.png)
    
    अब आपका कोड किसी भी उस अक्षर को छोड़ देता है जो वर्णमाला में नहीं है।

+ यह बेहतर होगा यदि आपका कोड वर्णमाला में ना होने वाला कुछ भी एन्क्रिप्ट नहीं करता है, लेकिन सिर्फ मूल अक्षर का उपयोग करता है।
    
    अपने कोड में `else` स्टेटमेंट जोड़ें, जो एन्क्रिप्टेड संदेश में सिर्फ मूल अक्षर जोड़ता है।
    
    ![स्क्रीनशॉट](images/messages-else.png)

+ अपने कोड का परीक्षण करें। आपको यह देखना है कि वर्णमाला के सभी अक्षर एन्क्रिप्ट किये गए है, लेकिन अन्यों को ऐसे ही छोड़ दिया गया है!
    
    ![स्क्रीनशॉट](images/messages-else-test.png)