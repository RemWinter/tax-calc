from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

@csrf_exempt
def calculate_net_pay(request):
  context = {}

  gross_salary = int(request.POST.get('gross_salary'))
  personal_allowance = 12570 
  basic_threshold = 50270
  higher_threshold = 125140

  # Calculate taxable income
  if gross_salary <= personal_allowance:
    context['net_salary'] = gross_salary
    return JsonResponse(context)  # No tax if income is below personal allowance

  # Calculate basic rate tax
  if  gross_salary <= basic_threshold:
    tax = (gross_salary - personal_allowance) * 0.20
  elif gross_salary <= higher_threshold:
    tax = (basic_threshold - personal_allowance) * 0.20 + (gross_salary - basic_threshold) * 0.40
  else:
    tax = (basic_threshold - personal_allowance) * 0.20 + (higher_threshold - basic_threshold) * 0.40 + (gross_salary - higher_threshold) * 0.45

  net_salary = gross_salary - tax
  context['net_salary'] = round(net_salary,2)

  return JsonResponse(context)