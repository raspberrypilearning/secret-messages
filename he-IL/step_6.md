## הצפנת הודעות שלמות

במקום להצפין ולפענח תו אחד בכל פעם, בואו נשנה את התוכנית כך שהיא תוכל להצפין הודעות שלמות!

+ ראשית, בדקו שהקוד שלכם נראה כך:
    
    ![צילום מסך](images/messages-character-finished.png)

+ צרו משתנה שיאחסן את ההודעה המוצפנת החדשה.
    
    ![צילום מסך](images/messages-newmessage.png)

+ שנו את הקוד כך שיאחסן את כל ההודעה של המשתמש ולא רק תו אחד.
    
    ![צילום מסך](images/messages-message.png)

+ הוסיפו לולאת `for` לקוד, והוסיפו הזחה (אידנטציה) לשאר הקוד כדי שהוא יעשה זאת על כל תו בהודעה.
    
    ![צילום מסך](images/messages-loop.png)

+ הריצו בדיקות על הקוד, אתם אמורים לראות שכל תו בהודעה מוצפן ומודפס למסך, אחד בכל שורה.
    
    ![צילום מסך](images/messages-loop-test.png)

+ בואו נוסיף כל תו מוצפן למשתנה `newMessage`.
    
    ![צילום מסך](images/messges-message-add-character.png)

+ אתם יכולים להדפיס את `newMessage` בזמן שהיא עוברת הצפנה.
    
    ![צילום מסך](images/messages-print-message-characters.png)

+ אם תמחקו את ההזחה שלפני הפקודה `print`, ההודעה המוצפנת תוצג רק פעם אחת בסוף. אתם יכולים גם למחוק את הקוד שמדפיס את התווים שהוצפנו.
    
    ![צילום מסך](images/messages-print-message-comment.png)