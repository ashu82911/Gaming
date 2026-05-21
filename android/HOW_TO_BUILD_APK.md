# 📱 How to Build Play&Win APK

## Prerequisites
- Android Studio (download from https://developer.android.com/studio)
- Java JDK 17+

## Steps to Build APK

### Step 1 — Open Project
1. Open Android Studio
2. Click "Open" → select this `android` folder

### Step 2 — Update URL
Open `app/src/main/java/com/playandwin/MainActivity.kt`
Change line:
```kotlin
private val APP_URL = "https://playandwin-ashu.streamlit.app"
```
Replace with your actual deployed Streamlit URL.

### Step 3 — Build Debug APK
- Menu → **Build → Build Bundle(s)/APK(s) → Build APK(s)**
- Wait ~2 minutes
- APK saved at: `app/build/outputs/apk/debug/app-debug.apk`

### Step 4 — Install on Android
- Copy `app-debug.apk` to your phone
- Enable "Install from unknown sources" in Settings
- Tap the APK file to install

## OR — Build via Command Line
```bash
cd android
./gradlew assembleDebug
```
APK will be at: `app/build/outputs/apk/debug/app-debug.apk`
