
using UnityEngine;

public class Rotator : MonoBehaviour
{
    public float rotationSpeed = 50.0f;

    private void Start()
    {
        Debug.Log("Rotator component started.");
    }

    private void Update()
    {
        RotateObject();
    }

    private void RotateObject()
    {
        transform.Rotate(Vector3.up * rotationSpeed * Time.deltaTime);
    }
}
