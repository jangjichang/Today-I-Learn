## adb command를 이용해 intent를 호출하여 화면을 실행하는 방법

## [adb](https://developer.android.com/studio/command-line/adb?hl=ko)

adb는 android debug bridge로 에뮬레이터 인스턴스나 연결된 Android 기기와 통신할 수 있는 다목적 명령줄 도구입니다.

command로 실행하기 때문에 윈도우 command를 사용해도 되고 안드로이드 스튜디오에 있는 커맨드 창에서 사용해도 됩니다.

공식 문서에는 'adb의 위치는 android_sdk/platform-tool'라고 설명하고 제 컴퓨터 기준으로 이 곳에 있습니다.

C:\Users\jcjang\AppData\Local\Android\Sdk\platform-tools

## 명령어

1. ```adb devices```
- 연결된 에뮬레이터/기기의 목록을 보여줍니다.

```
>>adb devices

List of devices attached
emulator-5554  device
emulator-5556  device
emulator-5558  device
```

2. ```adb shell```
- 연결된 에뮬레이터/기기에서 adb 원격 shell에 들어가거나 들어가지 않고도 adb를 통해 기기 명령을 실행할 수 있습니다.


shell에 들어가지 않고 단일 명령을 실행하려면 다음과 같은 shell 명령어를 사용합니다.

```
>>adb [-d|-e|-s serial_number] shell shell_command
```

또는 에뮬레이터/기기에서 다음과 같은 shell을 실행합니다.

```
>>adb [-d|-e|-s serial_number] shell
```

3. activity manager(am) 호출
- adb shell내에서 am 명령을 실행하여 activity시작, process 강제 중단, intent broadcast, 기기 화면 속성 수정 등 다양한 시스템 작업을 수행 할 수 있습니다.

```
>>am command
```

start 명령어에 대해 알아보겠습니다.

```
>>start [options] intent
```

이 명령어는 intent로 지정된 Activity를 시작합니다.

options으로는 <br/>
-D : 디버깅 활성화<br/>
-W : 실행이 완료되기를 기다립니다.<br/>
등등이 있습니다.

intent는 다음과 같이 지정할 수 있습니다.
```
-a action
```
intent 작업을 지정합니다 (예: android.intent.action.VIEW)

```
-d data_uri
```
intent data URI를 지정합니다. (예: cotent://contacts/people/1)

예를들어 myapp://goldenplanet?utm_source=google 라는 intent uri에서 android.intent.action.VIEW를 실행하고 싶다면 다음의 명령어를 실행하면 됩니다.

```
>>adb shell am start -W -a android.intent.action.VIEW -d myapp://goldenplanet?utm_source=google
```

intent-filter는 특정 intent를 받을지 말지를 정의하는 역할을합니다.

intent action과 inent uri는 AndroidManifest.xml에서 확인 할 수 있습니다.

```
<activity android:name=".MainActivity">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />

        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:host="goldenplanet"
            android:scheme="myapp" />
    </intent-filter>
</activity>
```
intent-filter tag가 2개 있는데, 위에는 MainActivity가 생성되면서 만들어진 tag입니다.

action tag는 허용된 intent action을 설정합니다.

intent action을 설정하지 않으면 요청한 intent를 처리할 수 없습니다.

예를 들어 여기서
```
<action android:name="android.intent.action.VIEW" />
<category android:name="android.intent.category.DEFAULT"/>
<category android:name="android.intent.category.BROWSABLE" />
<data
    android:host="goldenplanet"
    android:scheme="myapp" />
</intent-filter>
```

아래와 같이 action 설정이 없다면
```
<action android:name="android.intent.action.VIEW" />
```

아래와 같은 intent를 요청했을 때 intent를 처리 할 수 없습니다.
```
adb shell am start -W -a android.intent.action.VIEW -d myapp://goldenplanet?utm_source=google
```

왜냐하면 이 명령어의 -a (action)은 허용되지 않은 작업이기 때문에 intent를 처리할 수 없습니다.

마지막으로 data 필터는 데이터의 주소(uri)와 매칭되어야 합니다.

예제에서 사용한 uri는 myapp://goldenplanet?utm_source=google 와 같은 형태인데

myapp은 schme, goldenplanet은 host입니다.

데이터의 주소를 검사하는 uri는 다음과 같은 구조로 구성되어있습니다.

```
scheme://host:port/path
```

위와 같이 adb command를 이용해 intent를 호출하여 화면을 실행할 수 있습니다.

## 참고 페이지

[Android Debug Bridge](https://developer.android.com/studio/command-line/adb?hl=ko)

[intent](https://developer.android.com/guide/components/intents-filters?hl=ko)
