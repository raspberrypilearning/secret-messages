## Κρυπτογράφηση ολόκληρων μηνυμάτων

Αντί να κρυπτογραφείς και να αποκρυπτογραφείς τα μηνύματα ένα-ένα χαρακτήρα κάθε φορά, ας αλλάξουμε το πρόγραμμα για να κρυπτογραφήσουμε ολόκληρα μηνύματα!

+ Πρώτον, έλεγξε ότι ο κώδικας σου μοιάζει με αυτόν:
    
    ![screenshot](images/messages-character-finished.png)

+ Δημιούργησε μια μεταβλητή για να αποθηκεύσεις το νέο κρυπτογραφημένο μήνυμα.
    
    ![screenshot](images/messages-newmessage.png)

+ Άλλαξε τον κώδικά σου για να αποθηκεύσεις το μήνυμα του χρήστη και όχι μόνο ένα χαρακτήρα.
    
    ![screenshot](images/messages-message.png)

+ Πρόσθεσε ένα βρόχο `for` στον κώδικά σου και τοποθέτησε σε εσοχή το υπόλοιπο του κώδικα έτσι ώστε να επαναλαμβάνεται για κάθε χαρακτήρα του μηνύματος.
    
    ![screenshot](images/messages-loop.png)

+ Δοκίμασε τον κώδικά σου. Θα δεις ότι κάθε φορά κρυπτογραφείται και εμφανίζεται από ένας χαρακτήρας.
    
    ![screenshot](images/messages-loop-test.png)

+ Ας προσθέσουμε κάθε κρυπτογραφημένο χαρακτήρα στη μεταβλητή `newMessage`.
    
    ![screenshot](images/messges-message-add-character.png)

+ Μπορείς να `εμφανίζεις` το `newMessage` σταδιακά όσο κρυπτογραφείται.
    
    ![screenshot](images/messages-print-message-characters.png)

+ Εάν διαγράψεις τα κενά πριν από την εντολή `print`, το κρυπτογραφημένο μήνυμα θα εμφανιστεί μόνο μία φορά στο τέλος. Μπορείς επίσης να διαγράψεις τον κώδικα για την εμφάνιση των θέσεων χαρακτήρων.
    
    ![screenshot](images/messages-print-message-comment.png)