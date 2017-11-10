from django import forms


class MessageForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'class':'card mb-3',
                  'placeholder':'''পরিচয় গোপন করে সরাসরি বার্তা পাঠাতে এখানে লিখেই সেন্ড করুন। 
অবশ্য যদি কোন উত্তর বা রিপ্লাই আশা করেন তাহলে আপনার ইমেইল আইডিও এখানে দিতে পারেন। ''',
                   }
        ), required=True)