on run {targetBuddyPhone, targetMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetBuddyPhone of targetService
        set messageLength to count targetMessage
        set extensionLength to count ".png"
        if (text (messageLength - extensionLength + 1) thru messageLength of targetMessage = ".png") then
            set targetFile to (POSIX file targetMessage as alias)
            send targetFile to targetBuddy
        else
            send targetMessage to targetBuddy
        end if
    end tell
end run