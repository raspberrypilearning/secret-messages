## تشفير الرسائل بأكملها

بدلاً من تشفير الرسائل وفك تشفيرها حرفًا واحدًا في كل مرة ، دعنا نغير البرنامج لتشفير الرسائل بأكملها!

+ أولاً ، تحقق من أن الكود الخاص بك يبدو كالتالي:
    
    ![لقطة الشاشة](images/messages-character-finished.png)

+ قم بإنشاء متغير لتخزين الرسالة المشفرة الجديدة.
    
    ![لقطة الشاشة](images/messages-newmessage.png)

+ قم بتغيير الكود الخاص بك لتخزين رسالة المستخدم وليس مجرد حرف واحد.
    
    ![لقطة الشاشة](images/messages-message.png)

+ أضف حلقة ` for ` الى الكود الخاص بك، ثم ضع مسافة بادئة في بقية الكود بحيث يتكرر لكل حرف في الرسالة.
    
    ![لقطة الشاشة](images/messages-loop.png)

+ جرب الكود خاصتك. يجب أن ترى أن كل حرف في الرسالة تم تشفيره وطباعته حرفأ واحدأ في كل مرة.
    
    ![لقطة الشاشة](images/messages-loop-test.png)

+ دعنا نضيف كل حرف مشفر إلى متغير `newMessage `.
    
    ![لقطة الشاشة](images/messges-message-add-character.png)

+ يمكنك استخدام `print` مع `newMessage` بينما يجري تشفيرها.
    
    ![لقطة الشاشة](images/messages-print-message-characters.png)

+ ذا قمت بحذف المسافات قبل عبارة `print` ، سيتم عرض الرسالة المشفرة مرة واحدة فقط في النهاية. يمكنك أيضًا حذف كود طباعة مواضع الأحرف.
    
    ![لقطة الشاشة](images/messages-print-message-comment.png)