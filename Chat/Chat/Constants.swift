//
//  Constants.swift
//  Chat
//
//  Created by Devin Dhaliwal on 2/1/20.
//  Copyright © 2020 Devin Dhaliwal. All rights reserved.
//  Assisted by: https://learnappmaking.com/chat-app-ios-firebase-swift-xcode/

import Foundation
import Firebase

struct Constants
{
    struct refs
    {
        //refrences to database information
        static let databaseRoot = Database.database().reference()
        static let databaseChats = databaseRoot.child("chats")
    }
}
