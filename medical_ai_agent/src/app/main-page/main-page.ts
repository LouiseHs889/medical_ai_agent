import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Component({
  selector: 'app-main-page',
  standalone: false,
  templateUrl: './main-page.html',
  styleUrl: './main-page.scss'
})
export class MainPage implements OnInit{
constructor(private http:HttpClient){}
  @ViewChild('chatBox') private chatBoxRef!: ElementRef;
  ngOnInit(): void {
    
  }
  input_comment:any='';
  messages:{user:string;bot:string}[]=[]

  show(){
    const userInput=this.input_comment.trim();
    if(!userInput)
      return
    this.input_comment='';
    const inputMessage={user:userInput,bot:'AI思考中'};
    this.messages.push(inputMessage);
      const currentIndex = this.messages.length - 1;

    // 自動捲到底
    setTimeout(() => this.scrollToBottom(), 0);

    this.http.get<any>(`http://localhost:8000/kkk/${encodeURIComponent(userInput)}`)
      .subscribe({
        next: (res) => {
          const botReply = res?.apiapi || '⚠️ 無法取得回覆。';
          this.messages[currentIndex].bot = botReply.choices[0].message.content;
        },
        error: () => {
          this.messages[currentIndex].bot = '❌ 系統錯誤，請稍後再試。';
        }
      });
  // this.getData();
  }

  scrollToBottom() {
    if (this.chatBoxRef) {
      try {
        this.chatBoxRef.nativeElement.scrollTop = this.chatBoxRef.nativeElement.scrollHeight;
      } catch (err) {}
    }
  }

  ngAfterViewChecked(): void {
    this.scrollToBottom();
  }

}
