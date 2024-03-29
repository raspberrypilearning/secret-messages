## ಸೀಸರ್ ಸೈಫರ್ (The Caesar cipher)

ಸೈಫರ್ ಎನ್ನುವುದು ಒಂದು ರೀತಿಯ ರಹಸ್ಯ ಸಂಕೇತವಾಗಿದೆ, ಅಲ್ಲಿ ನೀವು ಅಕ್ಷರಗಳನ್ನು ವಿನಿಮಯ ಮಾಡಿಕೊಳ್ಳುವುದರಿಂದ ನಿಮ್ಮ ಸಂದೇಶವನ್ನು ಯಾರೂ ಓದಲಾಗುವುದಿಲ್ಲ.

ನೀವು ಒಂದು ಹಳೆಯ ಮತ್ತು ಅತ್ಯಂತ ಪ್ರಸಿದ್ಧ ಸೈಫರ್‌ಗಳಲ್ಲಿ **ಸೀಸರ್ ಸೈಫರ್** ಅನ್ನು ಬಳಸುತ್ತೀರಿ, ಇದನ್ನು ಜೂಲಿಯಸ್ ಸೀಸರ್ ಹೆಸರಿನಿಂದ ಇಡಲಾಗಿದೆ.

ನಾವು ಕೋಡಿಂಗ್ ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ಒಂದು ಪದವನ್ನು ಮರೆಮಾಡಲು ಸೀಸರ್ ಸೈಫರ್ ಅನ್ನು ಬಳಸಲು ಪ್ರಯತ್ನಿಸೋಣ.

+ ಪದ ಅಡಗಿಸುವುದನ್ನು**encryption** ಎಂದು ಕರೆಯುತ್ತಾರೆ.
    
    'a' ಅಕ್ಷರವನ್ನು ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡುವ ಮೂಲಕ ಪ್ರಾರಂಭಿಸೋಣ. ಇದನ್ನು ಮಾಡಲು, ನಾವು ವರ್ಣಮಾಲೆಯನ್ನು ವೃತ್ತದಲ್ಲಿ ಸೆಳೆಯಬಹುದು, ಈ ರೀತಿಯಾಗಿ:
    
    ![screenshot](images/messages-wheel.png)

+ ರಹಸ್ಯ ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಿದ ಪತ್ರವನ್ನು ಸಾಮಾನ್ಯದಿಂದ ಮಾಡಲು, ನೀವು ರಹಸ್ಯ ಕೀಲಿಯನ್ನು ಹೊಂದಿರಬೇಕು. 3 ನೇ ಸಂಖ್ಯೆಯನ್ನು ಕೀಲಿಯಾಗಿ ಬಳಸೋಣ (ಆದರೆ ನೀವು ಇಷ್ಟಪಡುವ ಯಾವುದೇ ಸಂಖ್ಯೆಯನ್ನು ನೀವು ಬಳಸಬಹುದು).
    
    'a' ಅಕ್ಷರವನ್ನು**encrypt** ಮಾಡಲು, ನೀವು ಕೇವಲ 3 ಅಕ್ಷರಗಳನ್ನು ಪ್ರದಕ್ಷಿನಕರವಾಗಿ ಸೇರಿಸಿದ್ದಾರೆ ನಿಮಗೆ 'd' ಅಕ್ಷರವನ್ನು ನೀಡುತ್ತದೆ:
    
    ![screenshot](images/messages-wheel-eg.png)

+ ಸಂಪೂರ್ಣ ಪದವನ್ನು ಎನ್ಕ್ರಿಪ್ಟ್ ಮಾಡಲು ನೀವು ಕಲಿತದ್ದನ್ನು ಬಳಸಬಹುದು. ಉದಾಹರಣೆಗೆ, 'hello' ಎನ್ಕ್ರಿಪ್ಟ್ ಮಾಡಿದಂತೆ 'khoor' ಆಗಿದೆ. ನೀವೇ ಪ್ರಯತ್ನಿಸಿ.
    
    + h + 3 = **k**
    + e + 3 = **h**
    + l + 3 = **o**
    + l + 3 = **o**
    + o + 3 = **r**

+ ಪಠ್ಯವನ್ನು ಸಹಜ ಸ್ಥಿತಿಗೆ ತರುವುದನ್ನು **decryption** ಎನ್ನುತ್ತಾರೆ. ಪದವನ್ನು ಡೀಕ್ರಿಪ್ಟ್ ಮಾಡಲು ಕೀಲಿಅನ್ನು ಸೇರಿಸುವ ಬದಲು ಕಳೆಯಿರಿ:
    
    + k - 3 = **h**
    + h - 3 = **e**
    + o - 3 = **l**
    + o - 3 = **l**
    + r - 3 = **o**