from fastapi import APIRouter
from database.db import get_db_connection
from pydantic import BaseModel

router = APIRouter()


class Customer(BaseModel):
    name: str
    phone: str
    email: str


@router.get("/health")
def health():
    return {"status": "Backend is healthy"}


@router.get("/customers")
def get_customers():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    connection.close()

    return [dict(customer) for customer in customers]


@router.post("/customers")
def create_customer(customer: Customer):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)",
        (customer.name, customer.phone, customer.email)
    )

    connection.commit()
    customer_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Customer created successfully",
        "id": customer_id
    }
class Invoice(BaseModel):
    customer_id: int
    amount: float
    status: str = "pending"


@router.post("/invoices")
def create_invoice(invoice: Invoice):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO invoices (customer_id, amount, status)
        VALUES (?, ?, ?)
        """,
        (invoice.customer_id, invoice.amount, invoice.status)
    )

    connection.commit()
    invoice_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Invoice created successfully",
        "id": invoice_id
    }
@router.get("/invoices")
def get_invoices():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM invoices")
    invoices = cursor.fetchall()

    connection.close()

    return [dict(invoice) for invoice in invoices]

class Payment(BaseModel):
    invoice_id: int
    amount: float
    status: str = "paid"


@router.post("/payments")
def create_payment(payment: Payment):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO payments (invoice_id, amount, status)
        VALUES (?, ?, ?)
        """,
        (payment.invoice_id, payment.amount, payment.status)
    )

    connection.commit()
    payment_id = cursor.lastrowid

    connection.close()

    return {
        "message": "Payment created successfully",
        "id": payment_id
    }

@router.get("/payments")
def get_payments():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM payments")
    payments = cursor.fetchall()

    connection.close()

    return [dict(payment) for payment in payments]
