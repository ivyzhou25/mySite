from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from .form import ImageForm, CourseForm
from .openai import process_image, choose_course
import os 

def home(request):
    return render(request, "pages/index.html")

def projects(request):
    return render(request, "pages/projects.html")


def contact(request):
    return render(request, "pages/contact.html")

def course(request):
    if request.method == 'POST':
        course1 = request.POST.get('course1')
        course2 = request.POST.get('course2')
        response = choose_course(course1, course2)
        #response = "I'm happy to help you decide between CS 3410 and CS 3420 for next fall. Let me gather course information and reviews from https://www.cureviews.org for both courses. Please give me a moment to retrieve the data.\n\n[Using open_url() to access the course introduction and reviews for CS 3410 and CS 3420]\n\nAfter reviewing the course introductions and student reviews, here is a comparison of CS 3410 and CS 3420:\n\nCS 3410 - Introduction:\n- Course Description: CS 3410 focuses on computer organization and programming, covering topics such as digital design, assembly language programming, and processor design.\n- Student Reviews: Positive reviews highlight the engaging lectures and hands-on projects that deepen understanding of computer organization.\n\nCS 3420 - Introduction:\n- Course Description: CS 3420 centers on the design and implementation of computer systems, including topics like operating systems, memory management, and network communication.\n- Student Reviews: Reviews for CS 3420 commend the comprehensive coverage of computer system design principles and the practical skills gained through assignments.\n\nBased on the information provided, here are some factors to consider in your decision:\n- If you are interested in delving into computer organization and design principles, CS 3410 might be a good fit.\n- If you want to explore the intricacies of computer system design and implementation, CS 3420 could be the course for you.\n\nUltimately, the decision between CS 3410 and CS 3420 depends on your specific interests and academic goals. I recommend considering the course content that aligns best with your interests and future pursuits. If you have any more questions or need further assistance, feel free to ask!"
        #response = response.replace("\n", "<br>")
        #response = "The comparison of cs 3410 and cs 3420: I'm sorry, but I cannot directly access or fetch data from external websites, including https://www.cureviews.org. However, I can provide you with some general information and guidance to help you make an informed decision between CS 3410 and CS 3420 based on their standard course descriptions and typical content. ### CS 3410: Computer System Organization and Programming CS 3410 covers topics such as computer architecture, assembly programming, and the design and implementation of a simple but functional microprocessor. The course is typically structured to give you a strong foundation in how hardware supports software. You'll likely delve into logic gates, CPU design, pipelining, memory hierarchy, and potentially some aspects of operating systems. Typical Prerequisites: Basic understanding of computer programming (usually in C or similar languages), discrete mathematics, and maybe some exposure to electronics. ### CS 3420: Embedded Systems CS 3420 focuses on designing and programming embedded systems, which are specialized computing systems that are part of larger mechanical or electrical systems (e.g., automotive control systems). This course often involves practical work with microcontrollers, real-time operating systems, and interfacing with sensors and actuators. Typical Prerequisites: Similar to CS 3410, though possibly with a stronger emphasis on practical hardware experience or concurrent work in related lab courses. ### Factors to Consider 1. **Interest and Career Goals**: - If you're more interested in understanding the theory and practice of computer architecture and want to focus on core computing systems, CS 3410 might be more suitable. - If you are fascinated by practical applications and want to work on systems that integrate both hardware and software in specific applications, CS 3420 could be more appealing. 2. **Teaching Style and Instructor**: - Review any available feedback on the instructors of these courses. Some may have different teaching styles that might suit you better. 3. **Course Load and Difficulty**: - Some students find one course more challenging than the other. Look into the syllabi, coursework, and assessments to see which aligns better with your strengths. 4. **Prerequisite Knowledge**: - Ensure you meet the prerequisites or have the required background knowledge to succeed in the course. ### Recommendations: - **Speak with Academic Advisors**: They can offer personalized advice based on your academic record and career aspirations. - **Talk to Peers**: Fellow students who have taken these courses can provide valuable insights. - **Review Feedback and Syllabi**: Look at course evaluations, reviews, and syllabi (which might be available through the Cornell course catalog or departmental websites). If you provide more specific details about your interests, goals, and background, I can offer more tailored advice!"
        index = response.find("\n")
        response = response[index:]
        print(response);
        return render(request, "pages/course_detail.html", {"course1": course1, "course2": course2, "resp" : response})
    else:
        form = CourseForm()
        return render(request, 'pages/course.html', {'form': form})

def product(request):
    if request.method == 'POST':
        #form = ImageForm(request.POST, request.FILES)
        img = request.FILES["file"]
        prompt = request.POST.get('prompt')
        resp = handle_uploaded_file(img, prompt)
        
        return render(request, "pages/product_detail.html", {"MEDIA_URL": settings.MEDIA_URL, "img": img, "resp" : resp})
    else:
        form = ImageForm()
        return render(request, 'pages/product.html', {'form': form})
    
def handle_uploaded_file(f, prompt):
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    
    file = os.path.join(settings.MEDIA_ROOT, f.name)
    with open(file, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    response = process_image(file, prompt)
    print (response.json())
    return response.json()['choices'][0]['message']['content']
            