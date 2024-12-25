from django.http import HttpResponse
from django.shortcuts import render



# def index(request):
#     return render(request,"index.html")
#     # params = {'name':'SANTOSH KAKAD', 'place':'Nagpur'}
#     # return render(request, 'index.html', params)
#     # return HttpResponse("Hello, welcome to my Django project!")
#     return render(request, "index.html")
def ones(request):
    return render(request, "one.html")


def analyze(request):
    # Get the text and checkbox value from GET request
    djText = request.POST.get('text', '')
    removepunc = request.POST.get('removepunc', 'default')
    cap = request.POST.get('cap', 'default')
    email = request.POST.get('email', '')
    
    success_message = "Welcome to the Text Utilies"
    # Define punctuation characters
    punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    
    if not djText or not email:
        # Render the form again with an error message if fields are empty
        return render(request, "one.html", {"error": "Please fill in both Email and Text fields."})
    
    # Initialize an empty string for the result
    analyze_result = ""

    # Remove punctuation if the checkbox is on
    if removepunc == "on":
        for char in djText:
            if char not in punctuation:
                analyze_result += char
        djText = analyze_result    
        show_text = True
    else :
        analyze_result = " "
        show_text = False
    
    # if cap == "on":
    #     cap = djText.upper()

    # Pass the analyzed text to the template
    return render(request, "analyze.html", {"analyze_text": djText, "email": email,"show_text": show_text, "success_message" :success_message})
# # def analyze(request):
# #     removepunc = request.GET.get("removepunc", "off")
# #     capitalize = request.GET.get("capitalized","off")
# #     djText = request.GET.get("text", "default")

# #     punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    
# #     analyze = ""
# #     if removepunc == "on":
# #         for char in djText:
# #             if char not in punctuation:
# #                 analyze += char
# #         djText = analyze
    
#     # if capitalize == "on":
#     #     for char in djText:
#     #         cap += char.upper()
    
#     # cap = ""
#     # if capitalize == "on":
#     #     analyze = djText.upper()
#     # params = {"purpose": "Removed Punctuations", "analyze_text": analyze}
#     # return render(request, "analyze.html", params)



# # def capitalizeFirst(request):
# #     return HttpResponse("capitalize First")


# # def newlineRemove(request):
# #     return HttpResponse("newlineRemove")

# # def spaceRemove(request):
# #     return HttpResponse("spaceRemove")


# # def charCount(request):
# #     return HttpResponse("charCount")
