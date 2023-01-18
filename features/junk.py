if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            print(messages)
            return redirect('apply_loan')                     
        user = User.objects.create_user(username=username, password=password)
        user.save()
        auth.login(request, user)
        
        user=User.objects.filter(username=request.user)
        print(user)
        form.fields['user'].initial = user.id
        form = LoanForm(request.POST)
        if form.is_valid():
            form.fields['user'] = user
            form.save()
            return redirect('dashboard')





