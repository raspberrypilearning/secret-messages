## पूर्ण संदेशों को इनक्रिप्ट करना

संदेशों को केवल एक बार में एक अक्षर एन्क्रिप्ट और डिक्रिप्ट करने के बजाय, चलो पूरे संदेशों को एन्क्रिप्ट करने के लिए प्रोग्राम को बदलते हैं!

+ सबसे पहले, जांचें कि आपका कोड इस तरह दिखता है:
    
    ![स्क्रीनशॉट](images/messages-character-finished.png)

+ नए एन्क्रिप्टेड संदेश को स्टोर करने के लिए एक वैरिएबल बनाएं।
    
    ![स्क्रीनशॉट](images/messages-newmessage.png)

+ अपना कोड बदलें ताकि उपयोगकर्ता का पूरा संदेश स्टोर हो, ना कि केवल एक अक्षर।
    
    ![स्क्रीनशॉट](images/messages-message.png)

+ अपने कोड में `for` लूप जोड़ें, और बाकी कोड को इंडेंट करें ताकि यह संदेश में प्रत्येक अक्षर के लिए दोहराया जाए।
    
    ![स्क्रीनशॉट](images/messages-loop.png)

+ अपने कोड का परीक्षण करें। आपको यह देखना चाहिए कि संदेश में प्रत्येक अक्षर एन्क्रिप्ट किया गया है और एक बार में एक ही प्रिंट किया गया है।
    
    ![स्क्रीनशॉट](images/messages-loop-test.png)

+ आइए प्रत्येक एन्क्रिप्ट किए गए अक्षर को अपने `newMessage` वेरिएबल में जोड़ें ।
    
    ![स्क्रीनशॉट](images/messges-message-add-character.png)

+ जैसे-जैसे `newMessage` एन्क्रिप्ट किया जा रहा है, आप इसे `print` कर सकते हैं।
    
    ![स्क्रीनशॉट](images/messages-print-message-characters.png)

+ यदि आप `print` से पहले रिक्त स्थान हटाते हैं, एन्क्रिप्टेड संदेश केवल एक बार अंत में प्रदर्शित किया जाएगा।आप अक्षर स्थितियों को प्रिंट करने वाला कोड भी हटा सकते हैं।
    
    ![स्क्रीनशॉट](images/messages-print-message-comment.png)