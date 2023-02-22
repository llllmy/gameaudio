using UnityEngine;
using UnityEngine.UI;
public class reverse : MonoBehaviour
{
    public Toggle toggle;
    public AK.Wwise.Event musicEvent;//正放事件
    public AK.Wwise.Event musicEventR;//倒放事件
    float maxDuration;
    float minDuration;
    uint musicr;
    uint music;
    int mPosition;//正放开始播放位置
    int mrPosition;//倒放开始播放位置
    int musicPosition;//正放结束播放位置
    int musicrPosition;//倒放结束播放位置
    int max;//事件长度（持续时间）毫秒
    void Start()
    {   
        toggle.onValueChanged.AddListener(OnToggleValueChanged);  
        
        AkUtilities.GetEventDurations(musicEvent.Id, ref maxDuration, ref minDuration);//获取长度,秒
      
        max = (int)(maxDuration*1000);//设置长度毫秒
    }
    private void Update()
    {
        AkSoundEngine.GetSourcePlayPosition(music, out musicPosition);//获取播放位置
        AkSoundEngine.GetSourcePlayPosition(musicr, out musicrPosition);
        mPosition = (max - musicrPosition);//设置开始播放位置
        mrPosition = (max - musicPosition);
    }
    void OnToggleValueChanged(bool isOn)
    {
        if (isOn)
        {
            if (mPosition == max)
            {
                mPosition = 65000;//初始时播放位置皆为0，max - musicrPosition = max(结尾），所以会直接播放结束，可以设置音频loop或设置mPosition == max时播放位置mPosition在哪里.
            }
            music = AkSoundEngine.PostEvent(musicEvent.Id, this.gameObject, 0x100000, MusicCallBack, null);//播放事件、获取事件信息
            AkSoundEngine.SeekOnEvent(musicEvent.Id, this.gameObject, mPosition, false);//设置Seek位置
        }
        else
        { 
            if (mrPosition == max)
            {
                mrPosition = 0;
            }
            musicr = AkSoundEngine.PostEvent(musicEventR.Id, this.gameObject, 0x100000, MusicCallBackR, null);
            AkSoundEngine.SeekOnEvent(musicEventR.Id, this.gameObject, mrPosition, false);
            
        }
    }

    void MusicCallBack(object in_cookie, AkCallbackType in_type, object in_info)
    {

    }
    void MusicCallBackR(object in_cookie, AkCallbackType in_type, object in_info)
    {
       
    }
}
